bool isAnagram(char * s, char * t){
    if (strlen(s) != strlen(t)){
        return false;
    }
    int c1[26] = {0};
    int c2[26] = {0};
    
    for (int i = 0; i < strlen(s); i++){
        c1[s[i] - 97] ++;
        c2[t[i] - 97] ++;
    }

    for (int i = 0; i < 26; i++){
        if (c1[i] != c2[i]){
            return false;
        }
    }
    return true;
}