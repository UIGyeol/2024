public class Cat extends Animal{
    public void informationCat(){
        name="Mandu";
        kind="cat";
        legCount=4;
        iq=100;
        System.out.println("이름: "+name+"종은"+kind+"다리 수는 "+legCount+"아이큐는"+iq);
    }
    public void MakeSound(){
        System.out.println("Meow Meow");
      }
    public void eatfood(){
        System.out.println("eatfood-cat");
      }
}
