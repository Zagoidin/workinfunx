#include <iostream>
#include <string>

int main() {
    std::string evA, posA; 
    int evCnt=0, uevCnt=0, posCnt=0, negCnt=0, sum=0, userCycleInt=0;
    std::cout<<"Num. of requests:\t";
    std::cin>>userCycleInt;
    std::cout<<"\n";
    for (int cycN = 0; cycN < userCycleInt; ++cycN){
        int ui;
        std::cout<<"Число #"<<cycN+1<<":\t";
        std::cin>>ui;
        sum = ui + sum;
        if(ui!=0){
            if(ui>0){posA = "positive";posCnt=posCnt+1;}else{posA = "negative";negCnt=negCnt+1;};
            if(ui%2==0){evA="even";evCnt+=1;}else{evA="uneven";uevCnt+=1;};
            std::cout<<"\t\x1b[2m"<<ui<<" is a "<<posA<<", "<<evA<<" number.\x1b[0m\n";
        }else{
            std::cout<<"\t\x1b[2m Zero is neither negative, positive, even nor uneven.\x1b[0m\n";
        }};
    std::cout<<"Result:\n\tEven:\t\t"<<evCnt<<";\n\tUneven:\t\t"<<uevCnt<<";\n\tPositive:\t"<<posCnt<<";\n\tNegative:\t"<<negCnt<<";\n\tSum:\t\t"<<sum<<'.';
    return 0;
}