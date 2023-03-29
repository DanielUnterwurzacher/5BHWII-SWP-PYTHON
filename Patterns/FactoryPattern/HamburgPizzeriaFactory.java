package Patterns.FactoryPattern;

public class HamburgPizzeriaFactory extends Pizzeria{ 

    @Override
    protected Pizza createPizza(String zuHolendePizza) {
        Pizza p = null; 
        if (zuHolendePizza.equals("HamburgSalami")) { 
            p = new HamburgSalami(); 
        } 
        else if (zuHolendePizza.equals("HamburgCalzone")) { 
            p = new HamburgCalzone(); 
        } 
        else if (zuHolendePizza.equals("HamburgDiavolo")) { 
            p = new HamburgDiavolo(); 
        } 
        else { 
            System.err.println("Ungültig!"); 
        } 
        return p;     
    }
}