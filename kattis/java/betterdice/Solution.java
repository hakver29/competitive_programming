package kattis.java.betterdice;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int list1_wins = 0;
        int list2_wins = 0;
        int n;
        List<Integer> list1 = new ArrayList<>();
        List<Integer> list2 = new ArrayList<>();

        n = scanner.nextInt();
        scanner.nextLine();

        String line1 = scanner.nextLine();
        String[] tokens1 = line1.trim().split("\\s+");
        for (String token : tokens1) {
            list1.add(Integer.parseInt(token));
        }

        String line2 = scanner.nextLine();
        String[] tokens2 = line2.trim().split("\\s+");
        for (String token : tokens2) {
            list2.add(Integer.parseInt(token));
        }

        for (int i = 0; i < n; i++) {
          for (int j = 0; j < n; j++) {
              if (list1.get(i) > list2.get(j)) {
                list1_wins += 1;
              } else if (list1.get(i) < list2.get(j)) {
                list2_wins += 1;
              }
          } 
        }

        if(list1_wins > list2_wins) {
          System.out.println("first");
        } else if(list1_wins < list2_wins ) {
          System.out.println("second");
        } else {
          System.out.println("tie");
        }

        scanner.close();
    }
}
