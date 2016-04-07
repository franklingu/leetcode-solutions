/**
 * Compare two version numbers version1 and version2.
 * If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
 * 
 * You may assume that the version strings are non-empty and contain only digits and the . character.
 * The . character does not represent a decimal point and is used to separate number sequences.
 * For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of
 *  the second first-level revision.
 * 
 * Here is an example of version numbers ordering:
 * 
 * 0.1 < 1.1 < 1.2 < 13.37
 */

public class Solution {
    public int compareVersion(String version1, String version2) {
        int start1 = 0, start2 = 0;
        int end1 = 0, end2 = 0;
        int tmp1, tmp2;
        while (end1 != -1 && end2 != -1) {
            end1 = version1.indexOf('.', start1);
            end2 = version2.indexOf('.', start2);
            if (end1 == -1 && end2 == -1) {
                tmp1 = Integer.parseInt(version1.substring(start1));
                tmp2 = Integer.parseInt(version2.substring(start2));
            } else if (end1 == -1) {
                tmp1 = Integer.parseInt(version1.substring(start1));
                tmp2 = Integer.parseInt(version2.substring(start2, end2));
            } else if (end2 == -1) {
                tmp1 = Integer.parseInt(version1.substring(start1, end1));
                tmp2 = Integer.parseInt(version2.substring(start2));
            } else {
                tmp1 = Integer.parseInt(version1.substring(start1, end1));
                tmp2 = Integer.parseInt(version2.substring(start2, end2));
            }
            if (tmp1 > tmp2) {
                return 1;
            } else if (tmp1 < tmp2) {
                return -1;
            }
            if (end1 == -1 && end2 == -1) {
                return 0;
            } else if (end1 == -1) {
                return 0 - checkRemainderPartOfVersion(version2.substring(end2 + 1));
            } else if (end2 == -1) {
                return checkRemainderPartOfVersion(version1.substring(end1 + 1));
            }
            start1 = end1 + 1;
            start2 = end2 + 1;
        }
        
        return 0;
    }
    
    private int checkRemainderPartOfVersion(String versionRemainder) {
        int start = 0, end = 0;
        while (end != -1) {
            end = versionRemainder.indexOf('.', start);
            if (end == -1) {
                if (Integer.parseInt(versionRemainder.substring(start)) != 0) {
                    return 1;
                } else {
                    return 0;
                }
            }
            if (Integer.parseInt(versionRemainder.substring(start, end)) != 0) {
                return 1;
            }
            start = end + 1;
        }
        
        return 0;
    }
}
