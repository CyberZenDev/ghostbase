from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ghostbase',
    version='1.1.0',
    description='SelfHosted DB',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/CyberZenDev/ghostbase',
    author='CyberZenDev',
    author_email='cyberzendev@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='flask sqlite database',
    packages=find_packages(),
    install_requires=['requests'],
)
