// ============================================================
// 30 - SOLID PRINCIPLES (tiny bad -> good examples)
// S: Single Responsibility
// O: Open/Closed
// L: Liskov Substitution
// I: Interface Segregation
// D: Dependency Inversion
// ============================================================

// ---------- S: Single Responsibility ----------
// BAD: one class does reporting + saving + printing.
class BadReport {
    String generate() { return "report"; }
    void save() { System.out.println("saved to file"); }
    void print() { System.out.println("printed"); }
}
// GOOD: three classes, each with ONE job.
class Report {
    String generate() { return "report"; }
}
class ReportSaver {
    void save(String s) { System.out.println("saved: " + s); }
}
class ReportPrinter {
    void print(String s) { System.out.println("printed: " + s); }
}

// ---------- O: Open/Closed ----------
// BAD: adding a shape means editing the area method.
class BadArea {
    double area(String shape, double v) {
        if (shape.equals("circle")) return 3.14 * v * v;
        if (shape.equals("square")) return v * v;
        return 0;                          // edit needed for each new shape
    }
}
// GOOD: open for extension (new subclass), closed for modification.
abstract class Shape {
    abstract double area();
}
class Circle extends Shape {
    double r;
    Circle(double r) { this.r = r; }
    double area() { return 3.14 * r * r; }
}

// ---------- L: Liskov Substitution ----------
// BAD: Rectangle's setHeight breaks Square's identity.
class Rectangle {
    int w, h;
    void setWidth(int w) { this.w = w; }
    void setHeight(int h) { this.h = h; }
    int area() { return w * h; }
}
class Square extends Rectangle {          // VIOLATES Liskov
    void setWidth(int w) { this.w = w; this.h = w; }
    void setHeight(int h) { this.w = h; this.h = h; }
}
// GOOD: unrelated classes; no surprising override.
class GoodSquare {
    int side;
    void setSide(int s) { side = s; }
    int area() { return side * side; }
}

// ---------- I: Interface Segregation ----------
// BAD: fat interface forces workers to implement eating.
interface RobotWorker {
    void work();
    void eat();                           // a robot does not eat
}
// GOOD: small, focused interfaces.
interface Worker {
    void work();
}
interface Eater {
    void eat();
}
class Human implements Worker, Eater {
    public void work() { System.out.println("human works"); }
    public void eat() { System.out.println("human eats"); }
}
class Robot implements Worker {
    public void work() { System.out.println("robot works"); }
}

// ---------- D: Dependency Inversion ----------
// BAD: high-level depends on a concrete low-level class.
class EmailService {
    void send(String msg) { System.out.println("email: " + msg); }
}
class BadNotifier {
    private EmailService email = new EmailService();
    void notify(String msg) { email.send(msg); }    // hardwired
}
// GOOD: depend on an abstraction.
interface MessageService {
    void send(String msg);
}
class EmailImpl implements MessageService {
    public void send(String msg) { System.out.println("email: " + msg); }
}
class SMSImpl implements MessageService {
    public void send(String msg) { System.out.println("sms: " + msg); }
}
class Notifier {
    private MessageService service;
    Notifier(MessageService service) { this.service = service; }  // injected
    void notify(String msg) { service.send(msg); }
}

public class Main {
    public static void main(String[] args) {
        // O
        System.out.println("Circle area: " + new Circle(2).area());

        // D
        Notifier n = new Notifier(new EmailImpl());
        n.notify("Hello");
        n = new Notifier(new SMSImpl());
        n.notify("Hello");
    }
}
