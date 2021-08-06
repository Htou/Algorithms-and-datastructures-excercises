import java.util.*;

public class LargestNumber {
    private static String largestNumber(String[] a) {
        //write your code here
        if (a.length == 0) {
            return "";
        }

        ArrayList<String> largestNumberList = new ArrayList<String>(Arrays.asList(a));

//        Collections.sort(largestNumberList, Collections.reverseOrder());

        largestNumberList.sort(new Comparator<String>() {
            @Override
            public int compare(String a, String b) {
                System.out.println(a + "-" + b);
                String order1 = a + b;
                System.out.println(b + "-" + a);
                String order2 = b + a;
                System.out.println(order2.compareTo(order1));
                return order2.compareTo(order1);
            }
        });

        String largestNumber = String.join("", largestNumberList);

        return largestNumber;
    }

    public static void main(String[] args) {
//        Scanner scanner = new Scanner(System.in);
//        int n = 2;
//        String[] a = new String[n];
//        a[0] = String.valueOf(21);
//        a[1] = String.valueOf(2);

//        String[] a = {"9", "4", "6", "1", "9"};

        String[] a = {"23", "39", "92"};

        System.out.println(largestNumber(a));
    }
}

