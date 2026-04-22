#include <memory>

class DynamicArray {
   private:
    std::unique_ptr<int[]> arr;
    int size;
    int capacity;

   public:
    DynamicArray(int capacity) {
        this->capacity = capacity;
        this->size = 0;
        this->arr = std::unique_ptr<int[]>(new int[capacity]);
    }

    int get(int i) { return arr[i]; }

    void set(int i, int n) { arr[i] = n; }

    void pushback(int n) {
        if (size == capacity) {
            resize();
        }

        arr[size] = n;
        size++;
    }

    int popback() {
        size--;
        return arr[size];
    }

    void resize() {
        capacity *= 2;
        std::unique_ptr<int[]> newArr(new int[capacity]);

        for (int i = 0; i < size; i++) {
            newArr[i] = arr[i];
        }

        arr = std::move(newArr);
    }

    int getSize() { return size; }

    int getCapacity() { return capacity; }
};
