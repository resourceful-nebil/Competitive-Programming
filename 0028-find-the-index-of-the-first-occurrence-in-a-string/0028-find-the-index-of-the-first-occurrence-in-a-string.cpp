class Solution {
public:
    int strStr(string haystack, string needle) {
        const int textLength = haystack.length();
        const int substringLength = needle.length();

        int i = 0;
        int j = 0;

        while (i < textLength){
            if (haystack[i] == needle[j]){
                i++;
                j++;
                if (j == substringLength ){
                    return i - j;
                }
            }else{
                i = i - j + 1;
                j = 0;
            }
        }
        return -1;
    }
};