#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-j2objc-annotations
Version  : 1.1
Release  : 2
URL      : https://repo1.maven.org/maven2/com/google/j2objc/j2objc-annotations/1.1/j2objc-annotations-1.1.jar
Source0  : https://repo1.maven.org/maven2/com/google/j2objc/j2objc-annotations/1.1/j2objc-annotations-1.1.jar
Source1  : https://repo1.maven.org/maven2/com/google/j2objc/j2objc-annotations/1.1/j2objc-annotations-1.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-j2objc-annotations-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-j2objc-annotations package.
Group: Data

%description data
data components for the mvn-j2objc-annotations package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/j2objc/j2objc-annotations/1.1
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/com/google/j2objc/j2objc-annotations/1.1

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/google/j2objc/j2objc-annotations/1.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/google/j2objc/j2objc-annotations/1.1


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/google/j2objc/j2objc-annotations/1.1/j2objc-annotations-1.1.jar
/usr/share/java/.m2/repository/com/google/j2objc/j2objc-annotations/1.1/j2objc-annotations-1.1.pom
