#include <iostream>
#include <vector>
#include <cmath>
#include <climits>
#include <algorithm>

using namespace std;

struct Point {
    int x, y;
};

bool compareX(Point p1, Point p2) {
    return p1.x < p2.x;
}

bool compareY(Point p1, Point p2) {
    return p1.y < p2.y;
}

float distance(Point p1, Point p2) {
    return sqrt((p1.x - p2.x)*(p1.x - p2.x) + (p1.y - p2.y)*(p1.y - p2.y));
}

float bruteForceClosestPair(vector<Point>& points, int& countComparisons) {
    float minDistance = FLT_MAX;
    int n = points.size();
    
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            countComparisons++; // counting comparisons
            float dist = distance(points[i], points[j]);
            minDistance = min(minDistance, dist);
        }
    }
    return minDistance;
}

float closestPairUtil(vector<Point>& points, int left, int right, int& countComparisons) {
    if (right - left <= 3) {
        return bruteForceClosestPair(points, countComparisons);
    }
    
    int mid = (left + right) / 2;
    Point midPoint = points[mid];
    
    float dl = closestPairUtil(points, left, mid, countComparisons);
    float dr = closestPairUtil(points, mid + 1, right, countComparisons);
    
    float minDist = min(dl, dr);
    
    vector<Point> strip;
    for (int i = left; i <= right; i++) {
        if (abs(points[i].x - midPoint.x) < minDist) {
            strip.push_back(points[i]);
        }
    }
    
    sort(strip.begin(), strip.end(), compareY);
    
    for (int i = 0; i < strip.size(); ++i) {
        for (int j = i + 1; j < strip.size() && (strip[j].y - strip[i].y) < minDist; ++j) {
            countComparisons++; // counting comparisons
            float dist = distance(strip[i], strip[j]);
            minDist = min(minDist, dist);
        }
    }
    
    return minDist;
}

float closestPair(vector<Point>& points, int& countComparisons) {
    sort(points.begin(), points.end(), compareX);
    return closestPairUtil(points, 0, points.size() - 1, countComparisons);
}

int main() {
    vector<Point> points = {{2, 3}, {12, 30}, {40, 50}, {5, 1}, {12, 10}, {3, 4}};
    
    int countComparisons = 0;
    float minDistance = closestPair(points, countComparisons);
    
    cout << "Minimum distance between two points: " << minDistance << endl;
    cout << "Number of comparisons: " << countComparisons << endl;

    return 0;
}

