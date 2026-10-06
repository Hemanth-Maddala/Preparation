// ============================================================
// 36 - OBSERVER PATTERN
// One-to-many notification. When the SUBJECT (publisher) changes,
// every OBSERVER (subscriber) is notified.
// ============================================================

import java.util.ArrayList;
import java.util.List;

// Observer side: anyone who wants to be notified.
interface Subscriber {
    void notify(String news);
}

class EmailSubscriber implements Subscriber {
    private String name;

    EmailSubscriber(String name) {
        this.name = name;
    }

    @Override
    public void notify(String news) {
        System.out.println(name + " got email: " + news);
    }
}

// Subject side: holds observers and notifies them.
class NewsPublisher {
    private List<Subscriber> subscribers = new ArrayList<>();

    void subscribe(Subscriber s) {
        subscribers.add(s);
    }

    void publish(String news) {
        for (Subscriber s : subscribers) {
            s.notify(news);            // push the news to everyone
        }
    }
}

public class Main {
    public static void main(String[] args) {
        NewsPublisher publisher = new NewsPublisher();

        EmailSubscriber ravi = new EmailSubscriber("Ravi");
        EmailSubscriber priya = new EmailSubscriber("Priya");

        publisher.subscribe(ravi);
        publisher.subscribe(priya);

        publisher.publish("Java 22 released");
    }
}
