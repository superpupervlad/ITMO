#include "circular_buffer.h" 

template<typename T> CB<T>::CB(int size_)
{
    size = size_;
    array = new T [size];
}

template<typename T> void CB<T>::pushright(T data)
{
    if (count == size)
        tail = ++tail % size;
    else
        count++;
    array[head] = data;
    head = ++head % size;
}

template<typename T> void CB<T>::pushleft(T data)
{
    if (tail == 0)
        tail = size - 1;
    else
        tail--;
    array[tail] = data;
    if (count != size)
        count++;
    else
        head = tail;
}

template<typename T> T CB<T>::popleft()
{
//     if (count == 0)
//         return NULL;
    unsigned temp = tail;
    tail = ++tail % size;
    count--;
    return array[temp];
}

template<typename T> T CB<T>::peekleft()
{   
//     if (count == 0)
//         return NULL;
    return array[tail];
}

template<typename T> T CB<T>::popright()
{
//     if (count == 0)
//         return NULL;
    if (head == 0)
        head = size - 1;
    else
        head--;
    count--;
    return array[head];
}

template<typename T> T CB<T>::peekright()
{
//     if (count == 0)
//         return NULL;
    if (head == 0)
        return array[size - 1];
    return array[head - 1];
}

template<typename T> T & CB<T>::operator[](unsigned int index)
{
    if (index <= count)
        return array[(head + index) % size];
    else
        return NULL;
}

template<typename T> void CB<T>::print()
{
    if (count == 0)
        std::cout << "Empty!\n";
    else{
        std::cout << array[tail] << " ";
        unsigned cur = (tail + 1) % size;
        while(cur != head){
            std::cout << array[cur] << " ";
            cur = ++cur % size;
        }
        std::cout << '\n';
    }
}

template<typename T> bool CB<T>::empty()
{
    return (count == 0);
}

template<typename T> void CB<T>::change_size(unsigned int new_size)
{
    T *new_buffer = new T [new_size];
    for(int i = 0; i < size or i < new_size; i++)
        new_buffer[i] = array[i];
    count =min(count, new_size);
    size = new_size;
    array = new_buffer;
    tail %= size;
    head %= size;
}

template<typename T> CBI<T>::CBI(T* position_, T* array_, unsigned int size_, T* start_, T* end_)
{
    position = position_;
    array = array_;
    start = start_;
    end = end_;
    size = size_;
}

template<typename T> CBI<T> CB<T>::begin()
{
    return CBI<T> (array + tail, array, size, array + tail, array + head - 1);
}

template<typename T> CBI<T> CB<T>::end()
{
    return CBI<T> (array + head, array, size, array + tail, array + head - 1);
}

template<typename T> CBI<T>::CBI(T* position_)
{
    position = position_;
}

