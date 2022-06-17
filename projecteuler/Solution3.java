package projecteuler;

import java.util.ArrayList;
import java.util.List;

/**
 * The prime factors of 13195 are 5, 7, 13 and 29.
 * 
 * What is the largest prime factor of the number 600851475143 ?
 */

public class Solution3 {
    public static void main(String[] args) {

        List<Integer> list = new ArrayList<>();
        long n = 600851475143L;
        int count = 2;
        while (n != 1) {
            if (n % count == 0) {

                list.add(count);
                n = n / count;
            } else {
                count++;
            }
        }

        list.stream().forEach(i -> {
            System.out.println(i);
        });

    }

}
