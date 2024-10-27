import java.util.Scanner;

public class PromotionExample {
    public static void main(String[] args) {
        byte byteValue = 10;
        int intValue = byteValue; 
        System.out.println("intValue: " + intValue); 

        Scanner scanner = new Scanner(System.in);
        String inputData;

        System.out.println("Enter text. Type 'q' to quit.");

        while (true) {
            inputData = scanner.nextLine();
            System.out.println("입력된 문자열: \"" + inputData + "\"");
            if (inputData.equals("q")) {
                break; 
            }
        }
        
        System.out.println("종료"); 
        scanner.close(); 
    }
}
