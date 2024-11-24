public class InheritanceAnimal {
    public static void main(String[] args) {
        Dog doggo=new Dog();
        Cat Kitty=new Cat();
        doggo.informationDog();
        doggo.MakeSound();
        doggo.eatfood();

        Kitty.informationCat();
        Kitty.MakeSound();
        Kitty.eatfood();
    }
    
}
