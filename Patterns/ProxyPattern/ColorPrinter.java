package Patterns.ProxyPattern;

public class ColorPrinter implements IDrucker {
    
    @Override
    public void drucken(String doc) {
        System.out.println("Color: " + doc);
    }

}
