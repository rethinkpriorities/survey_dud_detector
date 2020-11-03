import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
     name='survey_dud_detector',  
     version='0.2',
     author='Peter Hurford',
     author_email='peter@peterhurford.com',
     description='Automatically detect bad responses in survey responses',
     long_description=long_description,
	 long_description_content_type='text/markdown',
     url='https://github.com/rethinkpriorities/survey_dud_detector',
     packages=setuptools.find_packages(),
     classifiers=[
         'Development Status :: 3 - Alpha',
         'Programming Language :: Python :: 3',
         'License :: OSI Approved :: MIT License',
         'Operating System :: OS Independent',
     ],
 )
