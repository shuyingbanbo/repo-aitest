Name:           python-rabbitmq-amqp-python-client
Version:        0.1.0
Release:        1%{?dist}
Summary:        Python RabbitMQ client for AMQP 1.0 protocol
License:        Apache-2.0
URL:            https://github.com/rabbitmq/rabbitmq-amqp-python-client
Source0:        https://files.pythonhosted.org/packages/source/r/rabbitmq-amqp-python-client/rabbitmq_amqp_python_client-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pip

%description
Python RabbitMQ client for AMQP 1.0 protocol.
This library is in early stages of development and is meant to be used with RabbitMQ 4.0.


%package -n python3-rabbitmq-amqp-python-client
Summary:        Python RabbitMQ client for AMQP 1.0 protocol
Provides:       python-rabbitmq-amqp-python-client
Provides:       python3dist(rabbitmq-amqp-python-client) = %{version}
Requires:       python3-python-qpid-proton-0.39 >= 0.39.0
Requires:       python3-typing-extensions-4.13 >= 4.13.0

%description -n python3-rabbitmq-amqp-python-client
Python RabbitMQ client for AMQP 1.0 protocol.
This library is in early stages of development and is meant to be used with RabbitMQ 4.0.


%package help
Summary:        Documentation for python-rabbitmq-amqp-python-client
Requires:       python3-rabbitmq-amqp-python-client
Provides:       python3-rabbitmq-amqp-python-client-doc

%description help
Documentation and examples for python-rabbitmq-amqp-python-client.


%prep
%autosetup -n rabbitmq_amqp_python_client-%{version} -p1


%build
# poetry-core installed via pip to /usr/local; expose it to the build subprocess
export PYTHONPATH=/usr/local/lib/python3.11/site-packages:${PYTHONPATH}
pip3 wheel --no-build-isolation --no-deps -w wheelhouse .


%install
pip3 install --no-build-isolation --no-deps \
    --prefix=%{_prefix} --root %{buildroot} \
    wheelhouse/rabbitmq_amqp_python_client-%{version}*.whl


%files -n python3-rabbitmq-amqp-python-client
%license LICENSE
%{python3_sitelib}/rabbitmq_amqp_python_client/
%{python3_sitelib}/rabbitmq_amqp_python_client-%{version}*.dist-info/


%files help
%license LICENSE
%doc README.md


%changelog
* Thu May 28 2026 Python_Bot <Python_Bot@openeuler.org> - 0.1.0-1
- Initial package
