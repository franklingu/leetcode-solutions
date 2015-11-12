/**
 * All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG".
 * When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
 * 
 * Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
 * 
 * For example,
 * Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
 * Return:
 * ["AAAAACCCCC", "CCCCCAAAAA"].
 */

public class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        if (s.length() <= 10) {
            return new ArrayList<String>();
        }
        HashMap<String, Integer> mapping = new HashMap<String, Integer>();
        for (int i = 0; i <= s.length() - 10; i++) {
            String sub = s.substring(i, i + 10);
            if (mapping.containsKey(sub)) {
                mapping.put(sub, mapping.get(sub) + 1);
            } else {
                mapping.put(sub, 1);
            }
        }
        List<String> results = new ArrayList<String>();
        for (String str : mapping.keySet()) {
            if (mapping.get(str) > 1) {
                results.add(str);
            }
        }
        return results;
    }
}
