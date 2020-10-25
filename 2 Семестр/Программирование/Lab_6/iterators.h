#pragma once
#include <iostream>

template <class Iterator, class Predicate>
bool all_of(Iterator begin, Iterator end, Predicate p){
    for (auto cur = begin; cur != end; ++cur)
        if (!p(*cur))
            return false;
    return true;
}

template <class Iterator, class Predicate>
bool is_partitioned(Iterator begin, Iterator end, Predicate p){
    auto cur = begin;
    
    if (p(*cur)){
    for (; cur != end; ++cur)
        if (!p(*cur))
            break;
    for (; cur != end; ++cur)
        if (p(*cur))
            return false;
    }
    else{
        for (; cur != end; ++cur)
        if (p(*cur))
            break;
    for (; cur != end; ++cur)
        if (!p(*cur))
            return false;
    }
    return true;
}

template <class Iterator, class Predicate>
bool is_palindrome(Iterator begin, Iterator end, Predicate p){
    auto curb = begin;
    auto cure = end;
    cure--;
    while (curb < cure){
        if (p(*curb) != p(*cure))
            return false;
        ++curb; --cure;
    }
    return true;
}
        
