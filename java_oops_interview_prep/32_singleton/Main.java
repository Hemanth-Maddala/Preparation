// ============================================================
// 32 - SINGLETON
// One instance for the whole program. Modern thread-safe form:
// a private constructor + a static instance + static getter.
// ============================================================

class Logger {
    // Eager init: the JVM guarantees this field is created once,
    // and class-loading is thread-safe - no locks needed.
    private static final Logger INSTANCE = new Logger();

    private Logger() {          // nobody else can call new Logger()
        System.out.println("Logger created");
    }

    static Logger getInstance() {
        return INSTANCE;
    }

    void log(String msg) {
        System.out.println("[LOG] " + msg);
    }
}

public class Main {
    public static void main(String[] args) {
        // Both calls return the SAME object - constructor ran once.
        Logger l1 = Logger.getInstance();
        Logger l2 = Logger.getInstance();

        System.out.println("same instance? " + (l1 == l2));

        l1.log("hello");
    }
}
