You need to maintain a map for each character of the stream.
After that, you can also maintain a queue for the extraction of information.
Each character is inserted and removed from the queue at most once; hence time complexity is O(n).
Code looks something like
for (auto c : A)
{
mp[c]++;
q.push(c);
while (!q.empty() && mp[q.front()] > 1) q.pop();
if (!q.empty()) ans.push_back(q.front());
else ans.push_back(‘#’);
}

    TC: O(N)
    SC: O(1)