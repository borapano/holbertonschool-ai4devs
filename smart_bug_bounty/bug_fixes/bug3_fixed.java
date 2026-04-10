public class StudentGrades {

    public static void main(String[] args) {

        int[] grades = new int[5];

        for (int i = 0; i < grades.length; i++) {   // <-- FIXED
            grades[i] = i * 10;
        }

        int total = 0;

        for (int i = 0; i < grades.length; i++) {
            total += grades[i];
        }

        double average = total / grades.length;

        System.out.println("Average: " + average);
        System.out.println("Program finished");
    }
}