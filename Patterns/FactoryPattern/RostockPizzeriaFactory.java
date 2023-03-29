package Patterns.FactoryPattern;

public class RostockPizzeriaFactory extends Pizzeria{ 

    @Override
    protected Pizza createPizza(String zuHolendePizza) {
        Pizza p = null; 
        if (zuHolendePizza.equals("RostockSalami")) { 
            p = new RostockSalami(); 
        } 
        else if (zuHolendePizza.equals("RostockCalzone")) { 
            p = new RostockCalzone(); 
        } 
        else if (zuHolendePizza.equals("RostockDiavolo")) { 
            p = new RostockDiavolo(); 
        } 
        else { 
            System.err.println("Ungültig!"); 
        } 
        return p;     
    }
}