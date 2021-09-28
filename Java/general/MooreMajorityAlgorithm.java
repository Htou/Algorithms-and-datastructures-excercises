public class MooreMajorityAlgorithm {
    public static void main(String[] args) {
        int[] list = {1, 8, 7, 4, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2};

        int vote = 0;
        int counter = 0;

        for (int j = 0; j < list.length; j++) {
            if (counter == 0) {
                vote = list[j];
                counter = 1;
            } else if (vote == list[j]) {
                counter++;
            } else {
                counter--;
            }
        }

        System.out.println(vote);
    }
}
