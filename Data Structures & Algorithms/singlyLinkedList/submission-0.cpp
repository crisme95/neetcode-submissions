#include <memory>
#include <vector>

struct Node {
    int val;
    std::unique_ptr<Node> next;
};

class LinkedList {
   private:
    std::unique_ptr<Node> head;
    Node* tail;
    int size;

   public:
    LinkedList() {
        this->head = nullptr;
        this->tail = nullptr;
        this->size = 0;
    }

    int get(int index) {
        if (this->size < 1 || index < 0 || index > this->size - 1) {
            return -1;
        }

        Node* curr = this->head.get();
        int i = 0;

        while (curr->next.get() && i < index) {
            curr = curr->next.get();
            i++;
        }

        return curr->val;
    }

    void insertHead(int val) {
        std::unique_ptr<Node> newNode = std::make_unique<Node>();
        newNode->val = val;
        newNode->next = std::move(this->head);
        this->head = std::move(newNode);

        if (this->size < 1) {
            this->tail = this->head.get();
        }

        this->size++;
    }

    void insertTail(int val) {
        if (this->size < 1) {
            insertHead(val);
            return;
        }

        std::unique_ptr<Node> newNode = std::make_unique<Node>();
        newNode->val = val;
        newNode->next = nullptr;

        this->tail->next = std::move(newNode);
        this->tail = this->tail->next.get();
        this->size++;
    }

    bool remove(int index) {
        if (this->size < 1 || index < 0 || index > this->size - 1) {
            return false;
        }

        if (index == 0) {
            this->head = std::move(this->head->next);

            if (size == 1) {
                this->tail = nullptr;
            }

            this->size--;
            return true;
        }

        Node* curr = this->head.get();
        int i = 0;

        while (curr->next.get() && i < index - 1) {
            curr = curr->next.get();
            i++;
        }

        if (index == size - 1) {
            this->tail = curr;
        }

        if (curr->next) {
            curr->next = std::move(curr->next->next);
        }

        this->size--;
        return true;
    }

    std::vector<int> getValues() {
        std::vector<int> values;
        Node* curr = this->head.get();
        values.reserve(this->size);

        while(curr) {
            values.push_back(curr->val);
            curr = curr->next.get();
        }

        return values;
    }
};
