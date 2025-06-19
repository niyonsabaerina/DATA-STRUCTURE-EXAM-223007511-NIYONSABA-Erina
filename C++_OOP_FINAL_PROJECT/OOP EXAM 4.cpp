#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Denomination structure
struct Denomination {
    int value;
    int count;
};

// Base abstract class
class CashDispenser {
protected:
    Denomination* denoms;
    int size;

public:
    CashDispenser() : denoms(nullptr), size(0) {}

    virtual ~CashDispenser() {
        delete[] denoms;
    }

    virtual bool dispense(int amount) = 0;

    void addDenomination(int value, int count) {
        for (int i = 0; i < size; ++i) {
            if (denoms[i].value == value) {
                denoms[i].count += count;
                return;
            }
        }

        // Add new denomination
        Denomination* newDenoms = new Denomination[size + 1];
        for (int i = 0; i < size; ++i) {
            newDenoms[i] = denoms[i];
        }
        newDenoms[size].value = value;
        newDenoms[size].count = count;
        delete[] denoms;
        denoms = newDenoms;
        ++size;
    }

    void removeDenomination(int value) {
        int index = -1;
        for (int i = 0; i < size; ++i) {
            if (denoms[i].value == value) {
                index = i;
                break;
            }
        }

        if (index == -1) return; // Not found

        Denomination* newDenoms = new Denomination[size - 1];
        for (int i = 0, j = 0; i < size; ++i) {
            if (i != index) {
                newDenoms[j++] = denoms[i];
            }
        }
        delete[] denoms;
        denoms = newDenoms;
        --size;
    }

    void showDenoms() {
        for (int i = 0; i < size; ++i) {
            cout << denoms[i].value << " Rwf: " << denoms[i].count << " notes\n";
        }
    }
};

// Greedy Strategy
class GreedyDispenser : public CashDispenser {
public:
    bool dispense(int amount) override {
        cout << "\n[Greedy] Dispensing " << amount << " Rwf\n";
        for (int i = 0; i < size; ++i) {
            for (int j = i + 1; j < size; ++j) {
                if (denoms[j].value > denoms[i].value) {
                    swap(denoms[i], denoms[j]);
                }
            }
        }

        for (int i = 0; i < size; ++i) {
            int use = min(amount / denoms[i].value, denoms[i].count);
            if (use > 0) {
                cout << " - " << use << " x " << denoms[i].value << " Rwf\n";
                denoms[i].count -= use;
                amount -= use * denoms[i].value;
            }
        }

        if (amount > 0) {
            cout << "Not enough denominations to dispense remaining: " << amount << " Rwf\n";
            return false;
        }
        return true;
    }
};

// Optimal Strategy (fewest notes)
class OptimalDispenser : public CashDispenser {
public:
    bool dispense(int amount) override {
        cout << "\n[Optimal] Dispensing " << amount << " Rwf\n";
        vector<int> dp(amount + 1, 1e9);
        vector<int> last(amount + 1, -1);
        dp[0] = 0;

        for (int i = 0; i < size; ++i) {
            for (int c = 1; c <= denoms[i].count; ++c) {
                for (int j = amount; j >= denoms[i].value; --j) {
                    if (dp[j - denoms[i].value] + 1 < dp[j]) {
                        dp[j] = dp[j - denoms[i].value] + 1;
                        last[j] = i;
                    }
                }
            }
        }

        if (dp[amount] == 1e9) {
            cout << "Not possible to dispense optimally.\n";
            return false;
        }

        int a = amount;
        while (a > 0 && last[a] != -1) {
            int idx = last[a];
            cout << " - 1 x " << denoms[idx].value << " Rwf\n";
            denoms[idx].count--;
            a -= denoms[idx].value;
        }
        return true;
    }
};

int main() {
    CashDispenser* machines[2];

    GreedyDispenser* greedy = new GreedyDispenser();
    OptimalDispenser* optimal = new OptimalDispenser();

    // Add denominations
    greedy->addDenomination(5000, 5);
    greedy->addDenomination(2000, 4);
    greedy->addDenomination(1000, 10);

    optimal->addDenomination(5000, 5);
    optimal->addDenomination(2000, 4);
    optimal->addDenomination(1000, 10);

    machines[0] = greedy;
    machines[1] = optimal;

    // Try dispensing 13000 Rwf
    machines[0]->dispense(13000);
    machines[1]->dispense(13000);

    // Show remaining denominations
    cout << "\nRemaining Notes (Greedy):\n";
    greedy->showDenoms();

    cout << "\nRemaining Notes (Optimal):\n";
    optimal->showDenoms();

    // Clean up
    delete greedy;
    delete optimal;

    return 0;
}

