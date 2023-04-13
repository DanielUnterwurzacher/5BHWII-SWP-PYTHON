package Patterns.ProxyPattern;

public class Main {
    public static void main(String[] args){
        Drucker drucker = new Drucker();
        drucker.drucken("schwarz-weiß");

        drucker.switchTo(new ColorPrinter());
        drucker.drucken("farbe");
        
    }
}
