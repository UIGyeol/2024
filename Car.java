public class Car {
    int speed;
    int distance;
    String color;
    public Car(){

    }
    public void breakDown(){
        speed=speed-10;

    }
    public void speedUp(){
        speed=speed+5;
    }
    public int getCurrentSpeed(){
        return speed;
    }
    
}
