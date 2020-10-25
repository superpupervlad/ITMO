#pragma once
#include <iostream>
#include <iterator>
template<class T> class CB; // Буфер
template<class T> class CBI; // Итератор
#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))

template<class T>
class CB{
public:
    unsigned size;
    T *array;
    unsigned head = 0;
    unsigned tail = 0;
    unsigned count = 0;
    
    CB(int size_);
    ~CB() = default;
    void pushright(T data); // 1.Вставка в конец
    void pushleft(T data); // 2.Вставка в начало
    T popleft(); // 2.Удаление в начало
    T peekleft(); // 4.Доступ в начало 
    T popright(); // 1.Удаление в конец
    T peekright(); // 4.Доступ в конец
    //3. Вставка и удаление в произвольное место по итератору ???
    T& operator[](unsigned index); // 5.Доступ по индексу
    void print(); // Вывод
    void change_size(unsigned new_size); // 6. Изменение капасити
    bool empty(); // Проверка на пустоту внутри
    // Итераторы
    CBI<T> begin();
    CBI<T> end();
};

template<class T>//Удалить наследование??
class CBI : public std::iterator<std::random_access_iterator_tag, T>{
public:
    T* position;
    T* array;
    T* start;
    T* end;
    unsigned size;
    CBI(T* position_, T* array_, unsigned size_, T* start_, T* end_);
    CBI(T* position_);
    ~CBI() = default;
    T& operator*() {return *position;};
    T* operator->(){return position;}
    CBI& operator++(){
        ++position;
        return *this;
    }
    CBI operator++(int) {CBI tmp(*this); operator++(); return tmp;}
    CBI& operator--() {
        position--;
        return *this;}
    CBI operator--(int) {CBI tmp(*this); operator--(); return *this;}
    CBI operator-(typename std::iterator<std::random_access_iterator_tag, T>::difference_type iter){return CBI(position - iter);}
    bool operator==(const CBI& a) const {return position==a.position;}
    bool operator!=(const CBI& a) const {return position!=a.position;}
    typename std::iterator<std::random_access_iterator_tag, T>::difference_type operator-(const CBI<T>& iter){return position - iter.position;}
    typename std::iterator<std::random_access_iterator_tag, T>::difference_type operator+(CBI& iter){return position + iter.position;}
    CBI operator+(typename std::iterator<std::random_access_iterator_tag, T>::difference_type iter){return CBI(position + iter);}
    bool operator<(const CBI& a) {return position < a.position;}
    bool operator<(T* pointer){return position < pointer;}
    bool operator>(T* pointer){return position > pointer;}
    bool operator<=(T* pointer){return position <= pointer;}
    bool operator>=(T* pointer){return position >= pointer;}
    bool operator<=(const CBI& a) {return position <= a.position;}
    bool operator>(const CBI& a) {return position > a.position;}
    bool operator>=(const CBI& a) {return position >= a.position;}
    CBI& operator+=(typename std::iterator<std::random_access_iterator_tag, T>::difference_type iter){
            position += iter;
            return *this;
    }
    CBI& operator-=(typename std::iterator<std::random_access_iterator_tag, T>::difference_type iter){
            position -= iter;
            return *this;
    }
    CBI& operator=(const CBI& iter){
            position = iter.position;
            return *this;
    }
    CBI& operator=(T* iter){
            position = iter;
            return *this;
    }
};

