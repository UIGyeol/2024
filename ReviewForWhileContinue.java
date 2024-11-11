public class ReviewForWhileContinue {

    public static void main(String[] args) {
        ReviewForWhileContinue sample = new ReviewForWhileContinue();
        int sum = 0;
        int i = 0;
        for (i = 1; i <= 10; i++) {
            sum += i;
        }
        System.out.println("1~" + (i - 1) + " 합 : " + sum);
        sample.WhileAddFrom1To10();
        sample.BreakExample();
        sample.BreakOutterExample();
        sample.ContinueCounting();
    }

    public void WhileAddFrom1To10() {
        int i2 = 1;
        int sum2 = 0;
        while (i2 <= 10) {
            sum2 += i2;
            i2++; // Increment i2 to avoid an infinite loop
        }
        System.out.println("while문을 사용한 합: " + sum2);
    }

    public void BreakExample() {
        while (true) {
            int num = (int) (Math.random() * 6) + 1;
            System.out.println(num);
            if (num == 6) {
                break;
            }
        }
        System.out.println("프로그램 종료");
    }

    public void BreakOutterExample() {
        Outter: for (char upper = 'A'; upper <= 'Z'; upper++) {
            for (char lower = 'a'; lower <= 'z'; lower++) {
                System.out.println(upper + "-" + lower);
                if (lower == 'g') {
                    break Outter;
                }
            }
        }
        System.out.println("프로그램 실행종료");
    }
    public void ContinueCounting() {
        for(int i3;i3<=10;i3++){
            if(i3%2!=0){
                continue;
            }
            System.out.println(i3);
        }
    }
}
