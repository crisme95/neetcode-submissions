class DynamicArray {
   private:
    int* arr;
    unsigned int size;
    unsigned int capacity;

   public:
    DynamicArray(int capacity) {
        this->capacity = capacity;
        this->size = 0;
        this->arr = new int[capacity];
    }
    ~DynamicArray() {
        delete[] arr;
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
        int* newArr = new int[capacity];

        for (unsigned int i = 0; i < size; i++) {
            newArr[i] = arr[i];
        }

        delete[] arr;
        arr = newArr;
    }

    int getSize() { return size; }

    int getCapacity() { return capacity; }
};
