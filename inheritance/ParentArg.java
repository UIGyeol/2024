public class ParentArg {
    public ParentArg(String name){
        System.out.println("ParentArg("+name+")Constructor");
    }

    public ParentArg(InheritancePrint Obj){
        System.out.println("PatentArg(InheritancePrint)Constructor");
    }

    public void printName(){
        System.out.println("printName()- ParentArg");
    }
    
}
