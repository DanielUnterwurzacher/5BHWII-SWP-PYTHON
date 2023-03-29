package Patterns.FactoryPattern;

public class BerlinPizzeriaFactory extends Pizzeria{ 

    @Override
    protected Pizza createPizza(String zuHolendePizza) {
        Pizza p = null; 
        if (zuHolendePizza.equals("BerlinSalami")) { 
            p = new BerlinSalami(); 
        } 
        else if (zuHolendePizza.equals("BerlinCalzone")) { 
            p = new BerlinCalzone(); 
        } 
        else if (zuHolendePizza.equals("BerlinDiavolo")) { 
            p = new BerlinDiavolo(); 
        } 
        else { 
            System.err.println("Ungültig!"); 
        } 
        return p;     
    }
}