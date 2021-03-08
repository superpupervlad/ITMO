///
/// \param choice Function you want to calculate
/// \param n1 First number
/// \param n2 Second number
/// \return Result of calculating two numbers
/// \example processing_result('+', 1, 2) will return 3
float processing_result(char choice, float n1, float n2) {
    float res = 0;
    switch (choice) {
        case '1':
        case '+':
            res = n1 + n2; break;
        case '2':
        case '-':
            res =  n1 - n2; break;
        case '3':
        case '*':
            res =  n1 * n2; break;
        case '4':
        case '/':
            res =  n1 / n2; break;
    }
    return res;
}