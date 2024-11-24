public class InheritanceCasting {
    public static void main(String[] args) {
        InheritanceCasting inheritance = new InheritanceCasting();
        inheritance.objectCast2();
    }

    public void objectCast() {
        ParentCasting parent = new ParentCasting();
        ChildCasting child = new ChildCasting();

        // 업캐스팅 (자식 -> 부모): 항상 가능
        ParentCasting parent2 = child;

        // 다운캐스팅 (부모 -> 자식): 부모 객체가 자식 타입인 경우만 가능
        // 아래 코드는 런타임 오류(ClassCastException)가 발생할 수 있음
        ChildCasting child2 = (ChildCasting) parent; // 런타임 에러
    }

    public void objectCast2() {
        ChildCasting child = new ChildCasting();

        // 업캐스팅: 항상 가능
        ParentCasting parent2 = child;

        // 다운캐스팅: parent2가 실제로 ChildCasting 객체를 참조하므로 성공
        ChildCasting child2 = (ChildCasting) parent2;
    }
}

class ParentCasting {
    public void print() {
        System.out.println("ParentCasting print()");
    }
}

class ChildCasting extends ParentCasting {
    public void print() {
        System.out.println("ChildCasting print()");
    }

    public void childMethod() {
        System.out.println("ChildCasting only method");
    }
}
