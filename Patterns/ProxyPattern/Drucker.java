package Patterns.ProxyPattern;

public class Drucker implements IDrucker{
    private IDrucker drucker;

    public Drucker(){
        this.drucker = new SWPrinter();
    }

    @Override
    public void drucken(String doc) {
        this.drucker.drucken(doc);
    }

    public void switchTo(IDrucker drucker){
        this.drucker = drucker;
    }
}
