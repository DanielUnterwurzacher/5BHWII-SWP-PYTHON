package Patterns.ProxyPattern;

public class SWPrinter implements IDrucker {

    @Override
    public void drucken(String doc) {
        System.out.println("SW: " + doc);
    }
    
}
