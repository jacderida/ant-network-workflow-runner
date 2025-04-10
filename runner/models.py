from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Integer, String, DateTime, JSON, Boolean, ForeignKey
from sqlalchemy.orm import relationship, mapped_column
from sqlalchemy.orm.collections import attribute_mapped_collection
from sqlalchemy.orm import backref
from .database import Base

class WorkflowRun(Base):
    __tablename__ = "workflow_runs"

    id = Column(Integer, primary_key=True, index=True)
    workflow_name = Column(String, nullable=False)
    branch_name = Column(String, nullable=False)
    network_name = Column(String, nullable=False)
    triggered_at = Column(DateTime, nullable=False)
    inputs = Column(JSON, nullable=False)
    run_id = Column(Integer, nullable=False)

class Deployment(Base):
    __tablename__ = "deployments"

    id = Column(Integer, primary_key=True, index=True)
    workflow_run_id = Column(Integer, ForeignKey("workflow_runs.id"), nullable=False)
    name = Column(String, nullable=False)
    ant_version = Column(String)
    antnode_version = Column(String)
    antctl_version = Column(String)
    branch = Column(String)
    repo_owner = Column(String)
    chunk_size = Column(Integer)
    antnode_features = Column(String)
    peer_cache_node_count = Column(Integer)
    generic_node_count = Column(Integer, nullable=False)
    private_node_count = Column(Integer)
    enable_downloaders = Column(Boolean)
    uploader_count = Column(Integer)
    peer_cache_vm_count = Column(Integer)
    generic_vm_count = Column(Integer, nullable=False)
    private_vm_count = Column(Integer)
    client_vm_count = Column(Integer)
    peer_cache_node_vm_size = Column(String)
    generic_node_vm_size = Column(String, nullable=False)
    private_node_vm_size = Column(String)
    client_vm_size = Column(String)
    evm_network_type = Column(String, nullable=False)
    rewards_address = Column(String, nullable=False)
    max_log_files = Column(Integer)
    max_archived_log_files = Column(Integer)
    evm_data_payments_address = Column(String)
    evm_payment_token_address = Column(String)
    evm_rpc_url = Column(String)
    related_pr = Column(Integer)
    network_id = Column(Integer)
    description = Column(String)
    triggered_at = Column(DateTime, nullable=False)
    run_id = Column(Integer, nullable=False)
    region = Column(String, nullable=False, default="lon1")

    client_env = Column(String)
    node_env = Column(String)
    
    full_cone_private_node_count = Column(Integer)
    full_cone_private_vm_count = Column(Integer)
    full_cone_nat_gateway_vm_size = Column(String)

    symmetric_private_node_count = Column(Integer)
    symmetric_private_vm_count = Column(Integer)
    symmetric_nat_gateway_vm_size = Column(String)

class ClientDeployment(Base):
    __tablename__ = "client_deployments"

    id = Column(Integer, primary_key=True, index=True)
    workflow_run_id = Column(Integer, ForeignKey("workflow_runs.id"), nullable=False)
    name = Column(String, nullable=False)
    ant_version = Column(String)
    branch = Column(String)
    repo_owner = Column(String)
    chunk_size = Column(Integer)
    client_vm_count = Column(Integer, nullable=False, default=1)
    client_vm_size = Column(String, nullable=False, default="s-4vcpu-8gb")
    client_env = Column(String)
    evm_network_type = Column(String, nullable=False)
    evm_data_payments_address = Column(String)
    evm_payment_token_address = Column(String)
    evm_rpc_url = Column(String)
    network_id = Column(Integer)
    description = Column(String)
    related_pr = Column(Integer)
    triggered_at = Column(DateTime, nullable=False)
    run_id = Column(Integer, nullable=False)
    region = Column(String, nullable=False, default="lon1")
    provider = Column(String, nullable=False, default="digital-ocean")
    wallet_secret_key = Column(String)
    environment_type = Column(String, nullable=False)
    disable_download_verifier = Column(Boolean, default=False)
    disable_performance_verifier = Column(Boolean, default=False)
    disable_random_verifier = Column(Boolean, default=False)
    disable_telegraf = Column(Boolean, default=False)
    disable_uploaders = Column(Boolean, default=False)
    expected_hash = Column(String)
    expected_size = Column(String)
    file_address = Column(String)
    initial_gas = Column(String)
    initial_tokens = Column(String)
    max_uploads = Column(Integer)
    network_contacts_url = Column(String)
    peer = Column(String)
    uploaders_count = Column(Integer, nullable=False, default=1)

class ComparisonDeployment(Base):
    """Association table for many-to-many relationship between comparisons and test deployments"""
    __tablename__ = "comparison_deployments"

    id = Column(Integer, primary_key=True)
    comparison_id = Column(Integer, ForeignKey("comparisons.id"), nullable=False)
    deployment_id = Column(Integer, ForeignKey("deployments.id"), nullable=False)
    label = Column(String)
    
    comparison = relationship("Comparison", back_populates="test_deployments")
    deployment = relationship("Deployment")

class Comparison(Base):
    __tablename__ = "comparisons"

    id = Column(Integer, primary_key=True, index=True)
    ref_id = Column(Integer, ForeignKey("deployments.id"), nullable=False)
    description = Column(String)
    thread_link = Column(String)
    created_at = Column(DateTime, nullable=False)
    ref_label = Column(String)
    passed = Column(Boolean)

    ref_deployment = relationship("Deployment", foreign_keys=[ref_id])
    test_deployments = relationship("ComparisonDeployment", back_populates="comparison")
    
    # Instead of association_proxy, we can access deployments through the relationship
    @property
    def test_environments(self):
        return [(cd.deployment, cd.label) for cd in self.test_deployments]

@dataclass
class ComparisonSummary:
    id: int
    title: str
    created_at: datetime
    thread_link: Optional[str]
    description: Optional[str]

class SmokeTestResult(Base):
    __tablename__ = "smoke_test_results"

    id = Column(Integer, primary_key=True, index=True)
    deployment_id = Column(Integer, ForeignKey("deployments.id"), nullable=False)
    results = Column(JSON, nullable=False)
    created_at = Column(DateTime, nullable=False)

    deployment = relationship("Deployment", backref="smoke_test_results")

@dataclass
class RecentDeployment:
    id: int
    name: str
    created_at: datetime