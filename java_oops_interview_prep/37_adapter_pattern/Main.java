// ============================================================
// 37 - ADAPTER PATTERN
// Make an EXISTING class speak the interface the CALLER expects.
// Existing class -> Adapter -> Expected interface.
// ============================================================

// What the client (caller) expects.
interface Chargeable {
    void charge();
}

// An EXISTING class with an incompatible interface.
class UsbCharger {
    void plugUsb() {
        System.out.println("USB plugged in");
    }
}

// ADAPTER: wraps the existing class and implements the expected
// interface, translating the calls.
class UsbChargerAdapter implements Chargeable {
    private UsbCharger usbCharger;

    UsbChargerAdapter(UsbCharger usbCharger) {
        this.usbCharger = usbCharger;
    }

    @Override
    public void charge() {
        usbCharger.plugUsb();      // translate charge() -> plugUsb()
        System.out.println("Charging via adapter");
    }
}

public class Main {
    public static void main(String[] args) {
        // The client only knows Chargeable, and it works.
        Chargeable device = new UsbChargerAdapter(new UsbCharger());
        device.charge();
    }
}
