## http://disq.us/p/1g31b71
# interesting python solution
def solution(N):
    bg = max('{0:b}'.format(N).strip('0').split('1'))
    return 0 if bg == '' else len(bg)

## special case to verify N=1, N=2**n


# ## http://disq.us/p/1fnc2pv
# Java solution meets the time and space requirements
# public int solution(int N) {
#         int max = 0;
#         int gap = 0;
#         // first ignore all 0 from right
#         while ((N % 2) == 0) {
#             N /= 2;
#         }
#         // starts to count 0 after first 1 found
#         while (N > 0) {
#             if ((N % 2) == 0) {
#                 gap++;
#             } else {
#                 if (gap > max) {
#                     max = gap;
#                 }
#                 gap = 0;
#             }
#             N /= 2;
#         }

#         return max;
#     }
