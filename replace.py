#coding=utf-8
import os

# 在一行里面获取需要删除的属性
testLine = 'The resource R.string.avl_dialog_updateing appears to be unused'

def find_resource_in_a_line(pline):
	line = pline.strip()
	head = 'The resource R.string.'
	end = ' appears to be unused'
	return line[len(head): line.index(end)]

#print find_resource_in_a_line(testLine)


# 遍历所有文件
testPath = '/home/jet/Desktop/branches/supercleanv2/res/'
def list_file(rootDir,resource):
	for root,dirs,files in os.walk(rootDir):
		for filespath in files:
			file_path = os.path.join(root,filespath)
			del_resource(file_path,resource)
			
#list_file(testPath)


# 对文件中根据字符串对比后删除某行
def del_resource(file,resource):
	lines = open(file).readlines()
	for index,line in enumerate(lines):
		if resource in line:
			del lines[index]
			break
	open(file,"w").writelines(lines)

#testFile = '/home/jet/Desktop/lint.txt'
#res = '123'
#del_resource(testFile,res)

head = 'The resource R.string.'
lint_paths = '/home/jet/Documents/work/studio_workspace/branches/supercleanv2/res'
list_path = '/home/jet/Desktop/list_path/del_paths'


# 读取需要删除的文件的列表
lint_resources = open(list_path).readlines()
for lint_resource in lint_resources:
	print '资源行:',lint_resource
	if head in lint_resource:
		need_del_resource = find_resource_in_a_line(lint_resource)
		need_del_resource = '\"' + need_del_resource + '\"'
		print '需要删除的资源是',need_del_resource + '\n'
		list_file(lint_paths,need_del_resource)



