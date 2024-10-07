public class Solution {
    public int minLength(String s) {
        while (s.contains("AB") || s.contains("CD")) {
            String temp = s.replace("AB", "");
            temp = temp.replace("CD", "");
            s = temp;
        }
        return s.length();
    }
}