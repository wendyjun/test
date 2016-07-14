import os

if __name__ == "__main__":
	print '========================='
	os.chdir("/home/gxj/Downloads/oppo/oppo")
	os.system("/usr/local/bin/scrapy crawl oppo")
	print 'the end'
