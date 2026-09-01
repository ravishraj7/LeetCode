/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

void inorderHelper(struct TreeNode* node, int* arr, int* count) {
    if (node == NULL) {
        return;
    }
    inorderHelper(node->left, arr, count);
    arr[(*count)++] = node->val;
    inorderHelper(node->right, arr, count);
}

int countNodes(struct TreeNode* node) {
    if (node == NULL) {
        return 0;
    }
    return 1 + countNodes(node->left) + countNodes(node->right);
}

int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    int totalNodes = countNodes(root);
    int* result = (int*)malloc(totalNodes * sizeof(int));
    int count = 0;

    inorderHelper(root, result, &count);

    *returnSize = count;
    return result;
}