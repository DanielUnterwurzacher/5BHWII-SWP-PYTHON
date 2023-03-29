package Patterns.FactoryPattern;

public abstract class Pizzeria {
    public Pizza holePizza(String zuHolendePizza) { 
        Pizza p = createPizza(zuHolendePizza); 

        p.backen(); 
        p.schneiden(); 
        p.einpacken();

        return p; 
    } 

    protected abstract Pizza createPizza(String zuHolendePizza); 
}
