#include <iostream>
#include <vector>
#include <iterator>
#include <functional>
#include <numeric>
#include <string>

namespace {
template <class TIterator>
void IterSwap(TIterator a, TIterator b) {
    std::swap(*a, *b);
}

template <class TBidirectionanIterator>
void Reverse(TBidirectionanIterator first, TBidirectionanIterator last) {
    while ((first != last) && (first != --last)) {
        IterSwap(first++, last);
    }
}

inline int GetFatherIndex(int son) {
    return son >> 1;
}

inline int GetLeftSonIndex(int father) {
    return (father << 1) + 1;
}

inline int GetRightSonIndex(int father) {
    return (father + 1) << 1;
}

inline bool ExistsFatherIndex(int son) {
    return son > 0;
}

inline bool ExistsLeftSonIndex(int father, int size) {
    return GetLeftSonIndex(father) < size;
}

inline bool ExistsRightSonIndex(int father, int size) {
    return GetRightSonIndex(father) < size;
}

template <
    class TRandomAccessIterator,
    class TComparator = std::less<
        typename std::iterator_traits<TRandomAccessIterator>::value_type>
    >
void Heapify(TRandomAccessIterator begin,
             TRandomAccessIterator end,
             int index,
             TComparator comparator) {
    auto heap_size = end - begin;

    if (( ExistsRightSonIndex(index, heap_size)) &&
        (comparator(*(begin + GetRightSonIndex(index)), *(begin + index))) &&
        (comparator(*(begin + GetRightSonIndex(index)), *(begin +  GetLeftSonIndex(index))))
        ) {
        std::iter_swap(begin + index, begin + GetRightSonIndex(index));
        Heapify(begin, end, GetRightSonIndex(index), comparator);
    }

    if (( ExistsLeftSonIndex(index, heap_size)) &&
        (comparator(*(begin + GetLeftSonIndex(index)), *(begin + index)))
        ) {
        std::iter_swap(begin + index, begin + GetLeftSonIndex(index));
        Heapify(begin, end, GetLeftSonIndex(index), comparator);
    }
}

template <
    class TRandomAccessIterator,
    class TComparator = std::less<
        typename std::iterator_traits<TRandomAccessIterator>::value_type>
    >
void MakeHeap(TRandomAccessIterator begin,
              TRandomAccessIterator end,
              TComparator comparator) {
    auto heap_size = std::distance(begin, end);
    for (auto index = heap_size / 2; index >= 0; --index) {
        Heapify(begin, end, index, comparator);
    }
}


template <
    class TRandomAccessIterator,
    class TComparator = std::less<
        typename std::iterator_traits<TRandomAccessIterator>::value_type
        >
    >
void PopHeap(TRandomAccessIterator begin,
             TRandomAccessIterator end,
             TComparator comparator) {
    auto heap_size = std::distance(begin, end);
    IterSwap(begin, end - 1);
    --heap_size;

    int index = 0;
    int index_to_swap = -1;

    do {
        index_to_swap = -1;

        if ((ExistsRightSonIndex(index, heap_size)) &&
            (comparator(*(begin + GetRightSonIndex(index)), *(begin + GetLeftSonIndex(index)))) &&
            (comparator(*(begin + GetRightSonIndex(index)), *(begin + index)))
            ) {

            index_to_swap = GetRightSonIndex(index);
        }
        else if ((ExistsLeftSonIndex(index, heap_size)) &&
            (comparator(*(begin + GetLeftSonIndex(index)), *(begin + index)))
            ) {
            index_to_swap = GetLeftSonIndex(index);
        }

        if (index_to_swap >= 0) {
            IterSwap(begin + index, begin + index_to_swap);
            index = index_to_swap;
        }
    } while (index_to_swap >= 0);
}

template <
    class TRandomAccessIterator,
    class TComparator = std::less<
        typename std::iterator_traits<TRandomAccessIterator>::value_type>
    >
void PushHeap(
              TRandomAccessIterator begin,
              TRandomAccessIterator end,
              TComparator comparator
              ) {
    auto heap_size = std::distance(begin, end);

    auto index = heap_size - 1;
    auto me = begin + index , father = begin + GetFatherIndex(index);

    while (ExistsFatherIndex(index) &&
           (comparator(*me, *father))) {
        me = begin + index;
        father = begin + index / 2;

        IterSwap(me, father);
        index = GetFatherIndex(index);
    }
}
}  // namespace

template <
    class TRandomAccessIterator,
    class TComparator = std::less<
        typename std::iterator_traits<TRandomAccessIterator>::value_type>
    >
void Sort(
         TRandomAccessIterator begin,
         TRandomAccessIterator end,
         TComparator comparator = {}
         ) {
    auto tail = end;

    MakeHeap(begin, end, comparator);

    while (tail != begin) {
        PopHeap(begin, tail, comparator);
        --tail;
    }

    Reverse(begin, end);
}



template <class TElement, class TComparator = std::less<TElement>>
void Sort(std::vector<TElement>* vector, TComparator comparator = {}) {
    Sort(vector->begin(), vector->end(), comparator);
}
