package codewars;

import java.util.ArrayList;
import java.util.List;

/**
 * 
 * Convert number to reversed array of digits
 * Given a random non-negative number, you have to return the digits of this
 * number within an array in reverse order.
 */

public class Solution1 {

    public static void main(String[] args) {

    }

    public static int[] digitize(long n) {

        if (n==0) return new int[] {0};

        List<Integer> result = new ArrayList<>();
        long temp = 0;
        while (n != 0) {
            temp = n % 10;
            result.add((int)temp);
            n = n / 10;
        }

        return result.stream().mapToInt(i -> i).toArray();
    }
}
