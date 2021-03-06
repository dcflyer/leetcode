# -*- coding: utf-8 -*-
"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"


click to show corner cases.
Corner Cases: 

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

@author: n609874
"""

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        if not path: return path
            
        stack = ['/']
        for i in path.strip('/').split('/'):
            if '.' == i or '' == i:
                continue
#            WRONG !!! '..' may added to stackif len(stack) == 0
#            if '..' == i and len(stack) > 1:
            if '..' == i: 
                if len(stack) > 1: stack.pop()
            else:
                stack.append(i + '/')
        
        return "".join(stack).rstrip('/') if len(stack) > 1 else "".join(stack)

if __name__ == "__main__":
    test = Solution()
    print test.simplifyPath("/home/")
    print test.simplifyPath("/a/./b/../../c/")
    print test.simplifyPath("/../")