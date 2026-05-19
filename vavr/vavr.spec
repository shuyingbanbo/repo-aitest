Name:           vavr
Version:        2.0.6
Release:        1%{?dist}
Summary:        Java standard library extension built for Java 8 and above
BuildArch:      noarch
License:        Apache-2.0
URL:            https://github.com/vavr-io/vavr
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

%description
Javaslang (now known as Vavr) is a Java standard library extension
built for Java 8 and above. It provides persistent data types and
functional control structures.

%package -n javaslang
Summary:        Javaslang core library

%description -n javaslang
Core library of Javaslang, providing persistent data types and
functional control structures for Java 8+.

%package -n javaslang-match
Summary:        Javaslang annotation and processor for structural pattern matching

%description -n javaslang-match
Annotation and processor for structural pattern matching in Javaslang.

%package -n javaslang-pure
Summary:        Purely functional layer above Javaslang

%description -n javaslang-pure
A purely functional layer above the Javaslang core library.

%package -n javaslang-test
Summary:        Property check framework for Javaslang

%description -n javaslang-test
A property check framework for Javaslang.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%autosetup -n %{name}-%{version} -p1
# Disable benchmark module (not in default modules, but ensure it stays out)
# Remove release/signing plugins
%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin -r :maven-gpg-plugin
%pom_remove_plugin -r :jacoco-maven-plugin
# Remove scala-maven-plugin (code generator, requires Scala - skip gen profile)
%pom_remove_plugin -r :scala-maven-plugin
# Remove versions plugin (not needed for build)
%pom_remove_plugin -r :versions-maven-plugin
# Remove parent pom reference to sonatype oss-parent (not available offline)
%pom_remove_parent

# Map submodules to subpackages
%mvn_package ':javaslang' javaslang
%mvn_package ':javaslang-match' javaslang-match
%mvn_package ':javaslang-pure' javaslang-pure
%mvn_package ':javaslang-test' javaslang-test

%build
%mvn_build -f -- -DskipGen

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%files -n javaslang -f .mfiles-javaslang
%license LICENSE

%files -n javaslang-match -f .mfiles-javaslang-match
%license LICENSE

%files -n javaslang-pure -f .mfiles-javaslang-pure
%license LICENSE

%files -n javaslang-test -f .mfiles-javaslang-test
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Mon May 19 2026 Java_Bot <Java_Bot@openeuler.org> - 2.0.6-1
- Initial package
