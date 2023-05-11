typedef struct TreeNode {
    int data; // 노드에 저장할 데이터
    struct TreeNode *left; // 왼쪽 자식 노드를 가리키는 포인터
    struct TreeNode *right; // 오른쪽 자식 노드를 가리키는 포인터
} TreeNode;

// 이진 트리를 표현하는 구조체
typedef struct BinaryTree {
    TreeNode *root; // 이진 트리의 루트 노드를 가리키는 포인터
} BinaryTree;

BinaryTree *create_bts();
void insert_bts(BinaryTree *bts, int data);
TreeNode *insert_node(TreeNode *node, int data);
void preorder(TreeNode *node);
void inorder(TreeNode *node);
void postorder(TreeNode *node);