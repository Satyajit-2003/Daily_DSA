double average(int* salary, int salarySize){
    int sum = 0, max = salary[0], min = salary[0];
    for (int i = 0; i < salarySize; i++){
        if (salary[i] > max){
            max = salary[i];
        } else if(salary[i] < min){
            min = salary[i];
        } sum += salary[i];
    }

    return (double)(sum-min-max)/(salarySize-2);
}